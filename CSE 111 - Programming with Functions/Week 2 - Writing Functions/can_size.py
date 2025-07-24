
import math 


def main():
    can_name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    can_amount = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    
    for i in range(len(can_name)):
        name = can_name[i]
        radius = can_radius[i]
        height = can_height[i]
        amount = can_amount[i]
        volume = compute_volume(radius, height)
        area = compute_surface_area(radius, height)
        storage = compute_storage_efficiency(volume, area)
        cost = compute_cost_efficiency(volume, amount)
        print(f"Name: {name} | Radius: {radius:.2f} | Height: {height:.2f} | Amount: {amount} | Storage: {storage:.2f} | Cost: {cost:.0f}")

def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume


def compute_surface_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

def compute_storage_efficiency(volume, area):
    storage = volume / area
    return storage

def compute_cost_efficiency(volume, amount):
    cost = volume / amount
    return cost

main()