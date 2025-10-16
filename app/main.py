from fastapi import FastAPI
from database import Base, engine
from views import producto_view

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ejemplo MVC con FastAPI")

# Registrar rutas
app.include_router(producto_view.router)