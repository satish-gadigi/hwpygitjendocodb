from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        dbname="hwpygitjendocodb_db",
        user="satish",
        password="secret",
        host="db",   # service name from docker-compose.yml
        port="5432"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")

        try:
            conn = get_connection()
            print("Connected to:", conn.dsn)   # shows which DB, user, host, port
            conn.autocommit = True
            cur = conn.cursor()

            # Ensure table exists
            cur.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id SERIAL PRIMARY KEY,
                    text VARCHAR(255)
                );
            """)

            # Insert message
            cur.execute("INSERT INTO messages (text) VALUES (%s)", (message,))
            conn.commit()

            print("Inserted into DB:", message)  # ✅ inside try block

            cur.close()
            conn.close()

            return f"<h2>Inserted: {message}</h2><a href='/'>Insert another</a>"

        except Exception as e:
            print("Error during DB insert:", e)  # ✅ except block
            return f"<h2>Insert failed: {str(e)}</h2><a href='/'>Try again</a>"

    # GET request → show form
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
