from database import engine, Base
import models 

print("Building the database tables...")
Base.metadata.create_all(bind=engine)
print("Done! The tables are built! ")