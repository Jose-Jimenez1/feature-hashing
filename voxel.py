import pickle
import numpy as np
import matplotlib.pyplot as plt

def load_pickle_file(file_path):
    """
    Carga un archivo pickle que contiene datos voxelizados.
    """
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

def analyze_voxel_data(voxel_data):
    """
    Analiza los datos cargados para obtener información básica como
    los valores únicos y su distribución.

    Args:
        voxel_data (np.ndarray): Datos cargados desde el archivo pickle.
    
    Returns:
        tuple: Valores únicos y sus conteos.
    """
    unique_values, counts = np.unique(voxel_data, return_counts=True)
    print(f"Valores únicos: {unique_values}")
    print(f"Conteo de valores únicos: {counts}")
    return unique_values, counts

def reshape_to_cubic(data):
    """
    Reorganiza los datos en una forma cúbica si es posible.

    Args:
        data (np.ndarray): Datos unidimensionales.
    
    Returns:
        np.ndarray: Datos reorganizados en forma cúbica.
    
    Raises:
        ValueError: Si no es posible reorganizar los datos en un cubo exacto.
    """
    length = len(data)
    # Determinar el tamaño más cercano a un cubo
    side_length = int(round(length ** (1/3)))
    if side_length ** 3 == length:
        return data.reshape((side_length, side_length, side_length))
    else:
        raise ValueError("Los datos no pueden ser reorganizados en una forma cúbica exacta.")

def visualize_voxel_structure(voxel_data):
    """
    Representa gráficamente una estructura voxelizada en 3D.
    
    Args:
        voxel_data (np.ndarray): Matriz tridimensional de datos voxelizados.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Encuentra los índices de los voxeles activos (no nulos)
    x, y, z = np.where(voxel_data > 0)
    
    # Visualiza los voxeles
    ax.scatter(x, y, z, c='blue', marker='o')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.title("Estructura Cristalográfica Voxelizada")
    plt.show()

# Ruta del archivo pickle proporcionado por el usuario
file_path = '/mnt/data/mp-186.pkl'
try:
    # Cargar los datos del archivo pickle
    voxel_data = load_pickle_file(file_path)
    print(f"Datos cargados: Tipo {type(voxel_data)}, Tamaño {voxel_data.shape if isinstance(voxel_data, np.ndarray) else 'Desconocido'}")
    
    # Analizar los datos cargados
    unique_values, counts = analyze_voxel_data(voxel_data)
    
    # Reorganizar los datos en una forma cúbica
    voxel_data_cubic = reshape_to_cubic(voxel_data)
    print(f"Datos reorganizados a forma cúbica: {voxel_data_cubic.shape}")
    
    # Visualizar la estructura voxelizada
    visualize_voxel_structure(voxel_data_cubic)

except Exception as e:
    print(f"Error al procesar el archivo: {e}")
