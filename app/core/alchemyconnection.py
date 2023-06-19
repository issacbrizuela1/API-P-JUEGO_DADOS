from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class ALCHCONN(SQLAlchemy):
    
    def __init__(self, app: Incomplete | None = None, use_native_unicode: bool = True, session_options: Incomplete | None = None, metadata: Incomplete | None = None, query_class=..., model_class=..., engine_options: Incomplete | None = None) -> None:
        super().__init__(app, use_native_unicode, session_options, metadata, query_class, model_class, engine_options)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




# Configurar la conexión a la base de datos
engine = create_engine('mysql://root:@servidor/api_pruebas', echo=True)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Definir una clase que mapee a una tabla en la base de datos
Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    precio = Column(Integer)

    def __repr__(self):
        return f"<Producto(nombre='{self.nombre}', precio={self.precio})>"

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear un nuevo producto
nuevo_producto = Producto(nombre='Producto 1', precio=100)
session.add(nuevo_producto)
session.commit()

# Leer todos los productos
productos = session.query(Producto).all()
for producto in productos:
    print(producto)

# Actualizar un producto
producto_a_actualizar = session.query(Producto).filter_by(nombre='Producto 1').first()
producto_a_actualizar.precio = 150
session.commit()

# Eliminar un producto
producto_a_eliminar = session.query(Producto).filter_by(nombre='Producto 1').first()
session.delete(producto_a_eliminar)
session.commit()
