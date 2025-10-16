from sqlalchemy.orm import Session
from models.producto_model import Producto

def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def crear_producto(db: Session, nombre: str, descripcion: str, precio: float):
    nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False