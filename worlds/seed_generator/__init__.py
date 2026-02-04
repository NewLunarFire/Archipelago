import multiprocessing

from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, components, Type

from .GeneratorUI import launch

class GeneratorWorld(World):
    """
    Graphical seed generator for Archipelago 
    """
    game = "Seed Generator"
    hidden = True
    item_name_to_id = {}
    location_name_to_id = {}

def start_generator_process():
    process = multiprocessing.Process(target=launch)
    process.start()

components.append(Component("Generate (UI)", func=start_generator_process, description="Open the interactive seed generator.", component_type=Type.TOOL))
