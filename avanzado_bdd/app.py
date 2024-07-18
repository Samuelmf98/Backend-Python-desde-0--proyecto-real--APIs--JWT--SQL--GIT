from main import create_app
import os


app = create_app()

app.app_context().push() #permite tener un contexto general de todo el proyecto permitiendo accede a cualquier variable, paquete, modulo

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=os.getenv("PORT"), debug=True)

