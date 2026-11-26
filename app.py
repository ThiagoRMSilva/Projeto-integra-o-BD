import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados do SEU MySQL
DB = {
    "host": "localhost",
    "user": "root",
    "password": "",     
    "database": "roblox_db",
}


def conectar():
    return mysql.connector.connect(**DB)


def buscar_perguntas():
    """Lê as perguntas da tabela 'perguntas'. Usa a ÚLTIMA linha da tabela."""
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT pergunta_1, pergunta_2, pergunta_3 FROM perguntas")
    linhas = cur.fetchall()
    cur.close()
    con.close()
    if not linhas:
        return ["(pergunta 1 não cadastrada)", "(pergunta 2 não cadastrada)", "(pergunta 3 não cadastrada)"]
    return list(linhas[-1])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        con = conectar()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO respostas (nome, resposta1, resposta2, resposta3) "
            "VALUES (%s, %s, %s, %s)",
            (
                request.form["nome"],
                request.form["resposta1"],
                request.form["resposta2"],
                request.form["resposta3"],
            ),
        )
        con.commit()
        cur.close()
        con.close()
        return redirect(url_for("listar"))

    return render_template("cadastro.html", perguntas=buscar_perguntas())


@app.route("/listar")
def listar():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM respostas")
    respostas = cur.fetchall()
    cur.close()
    con.close()
    respostas.reverse()  # mostra as mais novas primeiro
    return render_template("listar.html", respostas=respostas, perguntas=buscar_perguntas())


@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM respostas WHERE id = %s", (id,))
    con.commit()
    cur.close()
    con.close()
    return redirect(url_for("listar"))


if __name__ == "__main__":
    app.run(debug=True)