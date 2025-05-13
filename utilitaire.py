from typing import Tuple
import time
from graphics import *

FPS = 60
DPF = 1/FPS

def millis_to_second(millis) -> float:
    return millis*(10**-3)

def second_to_millis(second) -> int:
    return int(second*(10**3))

def addition_tuple(tuple1, tuple2) -> Tuple[float, float]:
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]

def soustraction_tuple(tuple1, tuple2) -> Tuple[float, float]:
    return tuple1[0] - tuple2[0], tuple1[1] - tuple2[1]

def multiplication_tuple(tuple, x : float):
    return tuple.__class__([i*x for i in tuple])

def clamp(val, min_val, max_val):
    return min(max(val, min_val), max_val)

def sign(x : int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def moyenne_array(array):
    return sum(array)/len(array)

def min_array(array):
    mini = array[0]
    for i in range(1,len(array)):
        mini = min(mini, array[i])
    return mini

TIME_UNTIL_FPS_AVERAGE = 1.0
def frame_handling(act_time,TUFA_last_refresh,delta_time,last_chronos_time,frames,frame_array,displayed_frame_array):
    """
    Met à jour les variables necessaires pour faire tourner le jeu en respectant le nombre d'images par secondes.
    """
    
    if act_time - TUFA_last_refresh > TIME_UNTIL_FPS_AVERAGE:
        displayed_frame_array = frame_array.copy()
        TUFA_last_refresh = act_time
        frame_array.clear()
    time_to_wait = max(DPF - (time.time() - last_chronos_time), 0)
    time.sleep(time_to_wait)
    delta_time = time.time() - last_chronos_time
    last_chronos_time = time.time()
    if len(frame_array) >= FPS:
        frame_array.pop(0)
    frame_array.append(1 / delta_time)

    affiche_tout()

    return (act_time,TUFA_last_refresh,delta_time,last_chronos_time,frames,frame_array,displayed_frame_array)
