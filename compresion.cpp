#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

// Estructura para un punto 3D
struct Point {
    float x, y, z;

    // Constructor
    Point(float _x, float _y, float _z) : x(_x), y(_y), z(_z) {}
};

// Función hash para agrupar puntos
int hashFunction(float x, float y, float z, int gridSize) {
    int hx = static_cast<int>(x) / gridSize;
    int hy = static_cast<int>(y) / gridSize;
    int hz = static_cast<int>(z) / gridSize;
    return hx * 73856093 ^ hy * 19349663 ^ hz * 83492791; // Función hash
}

// Calcular el centroide de un grupo de puntos
Point calculateCentroid(const vector<Point>& points) {
    float cx = 0, cy = 0, cz = 0;
    for (const auto& p : points) {
        cx += p.x;
        cy += p.y;
        cz += p.z;
    }
    int n = points.size();
    return Point(cx / n, cy / n, cz / n);
}

// Comprimir puntos usando hashing
vector<Point> compressPoints(const vector<Point>& points, int gridSize) {
    unordered_map<int, vector<Point>> hashMap;

    // Agrupar puntos en celdas hash
    for (const auto& p : points) {
        int hashKey = hashFunction(p.x, p.y, p.z, gridSize);
        hashMap[hashKey].push_back(p);
    }

    // Calcular centroides de cada celda
    vector<Point> compressedPoints;
    for (const auto& entry : hashMap) {
        compressedPoints.push_back(calculateCentroid(entry.second));
    }

    return compressedPoints;
}

int main() {
    // Generar 27,000 puntos aleatorios (ejemplo)
    vector<Point> points;
    for (int i = 0; i < 27000; ++i) {
        points.emplace_back(rand() % 100, rand() % 100, rand() % 100);
    }

    // Primera compresión: 27,000 -> 256 puntos
    vector<Point> compressed256 = compressPoints(points, 10);

    // Segunda compresión: 256 -> 8 puntos
    vector<Point> compressed8 = compressPoints(compressed256, 50);

    // Mostrar los 8 puntos finales
    cout << "Puntos finales:" << endl;
    for (const auto& p : compressed8) {
        cout << "(" << p.x << ", " << p.y << ", " << p.z << ")" << endl;
    }

    // Pausa para evitar que la ventana se cierre
    cout << "Presiona cualquier tecla para salir..." << endl;
    cin.get();

    return 0;
}
