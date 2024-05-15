import import_stl_b

v_new = import_stl_b.process_vector([1, 2, 3])
if v_new != (1, 2, 3, 4):
    raise RuntimeError, v_new
