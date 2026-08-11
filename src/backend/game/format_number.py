def format_number(n):
    """
    Formatiert die übergebene Zahl in einen String, fügt ein suffix an, kürzt diesen und runded auf 2 Nachkommastellen.
    Genutzt aus Übersichtsgründen.
    Faktor 1000:
    * 1_000 -> 1.00K
    * 1_000_000 -> 1.00M
    * 1_000_000_000 -> 1.00B
    """
    
    suffixes = ["", "K", "M", "B", "T", "Qa", "Qi", "Sx", "Sp", "O", "N", "Dc", "UDc", "DDc", "TDc", "QaDc", "QiDc", "SxDc", "SpDc", "ODc"]
    
    if n == 0:
        return "0"
    
    # Bestimme den Index für das Suffix (jede Stufe ist 1000x größer)
    import math
    suj_index = 0
    if n > 0:
        suj_index = int(math.floor(math.log10(abs(n)) / 3))
    
    if suj_index >= len(suffixes):
        suj_index = len(suffixes) - 1
        
    if suj_index == 0:
        return str(int(n))
    
    scaled_value = n / (10 ** (3 * suj_index))
    
    return f"{scaled_value:.2f}{suffixes[suj_index]}"