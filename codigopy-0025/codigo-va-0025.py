# Emily Barraza NC = 0025

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
# Subir un nivel de 'codigo-va-0025.py' a 'EXA-VA-0025'
carpeta_proyecto = Path(__file__).resolve().parent.parent

# La imagen está en la raíz del proyecto y se llama img-original-0025.jpg
ruta_original = carpeta_proyecto / "img-original-0025.jpg"

# La carpeta de resultados dentro de codigopy-0025
carpeta_resultados = Path(__file__).resolve().parent / "resultado-img-0025"

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0025 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img0025 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_0025 = cv2.rotate(
    img0025, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0025.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0025 = cv2.warpAffine(
    img0025,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho
# y 500 píxeles de alto
img600x500_0025 = cv2.resize(
    img0025, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200
# píxeles sobre una copia de la imagen original
img_rojo_0025 = img0025.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0025,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("elefante original 0025", img0025)

cv2.imshow("elefante 90 0025", img90_0025)

cv2.imshow("elefante 45 0025", img45_0025)

cv2.imshow(
    "elefante 600x500 0025",
    img600x500_0025
)

cv2.imshow("elefante rojo 0025", img_rojo_0025)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-elefante1-0025.jpg"),
    img90_0025
)

cv2.imwrite(
    str(carpeta_resultados / "img-elefante2-0025.jpg"),
    img45_0025
)

cv2.imwrite(
    str(carpeta_resultados / "img-elefante3-0025.jpg"),
    img600x500_0025
)

cv2.imwrite(
    str(carpeta_resultados / "img-elefante4-0025.jpg"),
    img_rojo_0025
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()
print("Emily Barraza NC = 0025")