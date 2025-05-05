def time_zone(hours, timur_zone, artur_zone):
    return (hours + artur_zone - timur_zone) % 24

