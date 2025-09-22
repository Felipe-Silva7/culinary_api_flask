from app import create_app

app = create_app()

# Comentado pois a API rodará com gunicorn em produção
#if __name__ == "__main__":
#    app.run(debug=True)