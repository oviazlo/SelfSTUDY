import sys
import time
import queue


amphipods = ["A", "B", "C", "D"]
energy_per_type = dict(zip(amphipods, [1, 10, 100, 1000]))
# HEIGHT = 2
HEIGHT = 4

def print_coords(coords):
    text_to_print = list()
    text_to_print.append(list("# # # # # # # # # # # # #"))
    text_to_print.append(list("# . . . . . . . . . . . #"))
    for _ in range(HEIGHT):
        text_to_print.append(list("# # # . # . # . # . # # #"))
    text_to_print.append(list("    # # # # # # # # #    "))
    for i_am in amphipods:
        index = amphipods.index(i_am)
        for i in range(HEIGHT):
            text_to_print[HEIGHT + 1 - coords[index * HEIGHT + i][1]][2 + 2 * coords[index * HEIGHT + i][0]] = i_am
    for i_line in text_to_print:
        print(''.join(i_line))


def get_distance(coords1, coords2):
    if abs(coords1[0]-coords2[0]) == 0:
        return abs(coords1[1]-coords2[1])
    return abs(coords1[0]-coords2[0]) + abs(coords1[1]-HEIGHT) + abs(coords2[1]-HEIGHT)


def move_obj(coords, start_pos, end_pos):
    new_coords = coords.copy()
    distance = get_distance(start_pos, end_pos)
    energy = 0
    obj_type = get_type(coords, start_pos)
    energy = energy_per_type[obj_type] * distance
    new_coords[coords.index(start_pos)] = end_pos
    return new_coords, energy


def get_type(coords, pos):
    return amphipods[get_home_column(coords, pos)]


def get_home_column(coords, pos):
    if pos not in coords:
        return -1

    index = coords.index(pos)
    return int(index / HEIGHT)


def get_column_status(coords, column):
    """ return number of the correct occupants
        return -1 if column is occupied at least one species of wrong type
    """
    n_correct_objects = 0
    n_wrong_objects = 0
    column_coords = [(2+column*2, i) for i in range(HEIGHT)]
    for i_coord in column_coords:
        if i_coord in coords:
            if get_home_column(coords, i_coord) == column:
                n_correct_objects += 1
            else:
                n_wrong_objects += 1
    if (n_correct_objects + n_wrong_objects) == 0:
        return 0
    if n_wrong_objects > 0:
        return -1
    else:
        return n_correct_objects


def can_object_be_moved_home(coords, pos):
    home_column = get_home_column(coords, pos)
    column_status = get_column_status(coords, home_column)
    if column_status < 0:
        return False

    # check if it can move through hallway
    x_coord_column = get_column_x_coord(get_home_column(coords, pos))
    if pos[0] < x_coord_column:
        number_of_objects_on_the_way = sum([(i, HEIGHT) in coords for i in range(pos[0]+1, x_coord_column)])
    else:
        number_of_objects_on_the_way = sum([(i, HEIGHT) in coords for i in range(x_coord_column, pos[0])])

    number_of_objects_on_the_way += sum([(pos[0], i) in coords for i in range(pos[1]+1, HEIGHT)])

    if number_of_objects_on_the_way == 0:
        return True
    else:
        return False


def is_in_hallway(coords, pos):
    if pos[1] == HEIGHT:
        return True
    else:
        return False


def get_range_of_available_positions_in_hallway(coords, pos):
    number_of_objects_above = sum([(pos[0], i) in coords for i in range(pos[1]+1, HEIGHT)])
    if number_of_objects_above > 0:
        return []

    available_positions = []
    rightmost_available_index = pos[0]
    leftmost_available_index = pos[0]
    while True:
        if ((rightmost_available_index+1, HEIGHT) not in coords) and ((rightmost_available_index + 1) <= 10):
            if (rightmost_available_index + 1) not in [2, 4, 6, 8]:
                available_positions.append((rightmost_available_index + 1, HEIGHT))
            rightmost_available_index += 1
        else:
            break
    while True:
        if ((leftmost_available_index-1, HEIGHT) not in coords) and ((leftmost_available_index - 1) >= 0):
            if (leftmost_available_index - 1) not in [2, 4, 6, 8]:
                available_positions.append((leftmost_available_index - 1, HEIGHT))
            leftmost_available_index -= 1
        else:
            break
    return sorted(available_positions)


def get_column_x_coord(column):
    return 2+2*column


def is_home(coords, pos):
    home_column = get_home_column(coords, pos)
    x_coords = get_column_x_coord(home_column)
    if pos[0] == x_coords:
        return True
    else:
        return False


def get_all_available_movement(coords):
    available_moves = []
    for i_coord in coords:
        # is home for the selected element and all element below it
        if sum(not is_home(coords, (i_coord[0],i)) for i in range(0,i_coord[1]+1)) == 0:
            continue
        home_column = get_home_column(coords, i_coord)
        x_coords = get_column_x_coord(home_column)
        can_move_home = can_object_be_moved_home(coords, i_coord)
        if can_move_home:
            n_filled_at_home = get_column_status(coords, home_column)
            available_moves.append((i_coord, (x_coords, n_filled_at_home)))
        elif i_coord[1] != HEIGHT:
            number_of_objects_above = sum([(i_coord[0], i) in coords for i in range(i_coord[1] + 1, HEIGHT)])
            if number_of_objects_above == 0:
                available_moves += [(i_coord, x) for x in get_range_of_available_positions_in_hallway(coords, i_coord)]
    return available_moves


def is_everyone_home(coords):
    for i_coords in coords:
        if i_coords[1] == HEIGHT:
            return False
    return True


def get_n_objects_in_corridor(coords):
    n_in_corr = 0
    for i_coords in coords:
        if i_coords[1] == HEIGHT:
            n_in_corr += 1
    return n_in_corr


def get_n_objects_that_got_home(coords):
    n_out = 0
    for i_coords in coords:
        column = get_home_column(coords, i_coords)
        x_column_x = get_column_x_coord(column)
        if x_column_x == i_coords[0]:
            n_out += 1
    return n_out


def get_hash(coords):
    out_hash = ""
    for i in range(4):
        selected_line = [coords[HEIGHT*i+k] for k in range(HEIGHT)]
        sorted_coord_line = sorted(selected_line)
        for j in range(HEIGHT):
            out_hash += str(sorted_coord_line[j][0])
            out_hash += str(sorted_coord_line[j][1])
    return out_hash

def parse_coord_map(str_coord_map):
    # tmp_str_list = ["#AA.D.B.B.BD#", "###B#.#.#.###", "#D#.#C#.#", "#D#.#C#C#", "#A#.#C#A#"]
    out_coords = []
    for i_am in amphipods:
        for i in range(HEIGHT+1):
            line = str_coord_map[i]
            counter = 2
            first_symbol_found = False
            if i==0:
                counter = 0
            for i_char in list(line):
                if i_char != "#" and not first_symbol_found:
                    first_symbol_found = True
                if first_symbol_found:
                   if i_char == i_am:
                       out_coords.append((counter, HEIGHT-i))
                   counter += 1
    return out_coords


# task 1
# coords = [
#     (4, 0), (6, 1),  # A
#     (2, 0), (8, 1),  # B
#     (2, 1), (8, 0),  # C
#     (4, 1), (6, 0),  # D
# ]

# task 2
coords = [
    (4,0), (6,3), (6,1), (8,2), # A
    (2,0), (4,1), (6,2), (8,3), # B
    (2,3), (4,2), (8,0), (8,1), # C
    (2,1), (2,2), (4,3), (6,0), # D
]

# example 2
# coords = [
#     (2,0), (6,1), (8,0), (8,2), # A
#     (2,3), (4,1), (6,2), (6,3), # B
#     (4,2), (4,3), (6,0), (8,1), # C
#     (2,1), (2,2), (4,0), (8,3), # D
# ]

stack = queue.Queue()  # coords, energy
stack.put((coords, 0))
hash_map = dict()
hash_map[get_hash(coords)] = 0

print_coords(coords)
print()

final_energy = 9999999

t0 = time.time()

while not stack.empty():

    coords, energy = stack.get()

    available_moves_init = get_all_available_movement(coords)

    for move in available_moves_init:
        start_pos = move[0]
        end_pos = move[1]
        new_coords, step_energy = move_obj(coords, start_pos, end_pos)
        new_total_energy = energy + step_energy
        new_hash = get_hash(new_coords)
        if new_hash in hash_map:
            hashed_energy = hash_map[new_hash]
            if new_total_energy >= hashed_energy:
                continue

        hash_map[new_hash] = new_total_energy

        stack.put((new_coords, new_total_energy))

    if (len(available_moves_init) == 0) and (is_everyone_home(coords)):
        if energy < final_energy:
            final_energy = energy
            print("Final energy: ", final_energy)

print("Hash map size: ", len(hash_map))
exec_time = time.time()-t0
print("EXEC. TIME: ", exec_time)