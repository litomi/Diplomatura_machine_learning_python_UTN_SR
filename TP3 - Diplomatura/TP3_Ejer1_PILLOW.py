from PIL import Image as mg

(mg.new('RGB', (600, 800), (255, 0, 0))).save('imagenes/roja.jpeg')
(mg.new('RGB', (600, 800), (0, 255, 0))).save('imagenes/verde.jpeg')
(mg.new('RGB', (600, 800), (255, 233, 0))).save('imagenes/amarilla.jpeg')

