from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from controllers import producto_controller

router = APIRouter(prefix="/productos", tags=["Productos"])

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_productos(db: Session = Depends(get_db)):
    return producto_controller.obtener_productos(db)

@router.get("/{producto_id}")
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = producto_controller.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/")
def crear_producto(nombre: str, descripcion: str, precio: float, db: Session = Depends(get_db)):
    return producto_controller.crear_producto(db, nombre, descripcion, precio)

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    eliminado = producto_controller.eliminar_producto(db, producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado correctamente"}