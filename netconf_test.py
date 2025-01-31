from ncclient import manager

# Datos de conexión al router CSR1000v
router = {
    "host": "192.168.1.100",  # IP asignada a Loopback0
    "port": 830,  # Puerto NETCONF
    "username": "cisco",
    "password": "cisco123",
    "hostkey_verify": False
}

# Intentar conexión NETCONF
try:
    with manager.connect(**router) as m:
        print("¡Conexión NETCONF exitosa!")
        print("Capacidades soportadas por el router:")
        for capability in m.server_capabilities:
            print(capability)
except Exception as e:
    print(f"Error en la conexión: {e}")

