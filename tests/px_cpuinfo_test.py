import os

from px import px_cpuinfo


def test_get_core_count():
    physical, logical = px_cpuinfo.get_core_count()

    assert physical >= 1
    assert logical >= physical
    assert logical % physical == 0


def test_get_core_count_from_proc_cpuinfo():
    my_dir = os.path.dirname(__file__)

    physical, logical = px_cpuinfo.get_core_count_from_proc_cpuinfo(
        os.path.join(my_dir, "proc-cpuinfo-2p4l"))
    assert physical == 2
    assert logical == 4

    physical, logical = px_cpuinfo.get_core_count_from_proc_cpuinfo(
        os.path.join(my_dir, "proc-cpuinfo-1p1l"))
    assert physical == 1
    assert logical == 1

    # This one is from my cell phone, just to provide a weird corner case example of things
    # we may have to handle.
    physical, logical = px_cpuinfo.get_core_count_from_proc_cpuinfo(
        os.path.join(my_dir, "proc-cpuinfo-8p8l"))
    assert physical == 8
    assert logical == 8

    assert px_cpuinfo.get_core_count_from_proc_cpuinfo("/does/not/exist") is None


def test_get_core_count_from_sysctl():
    test_me = px_cpuinfo.get_core_count_from_sysctl()
    if test_me is None:
        # We're likely on Linux
        return

    # Sanity check, since we don't know the answer this is the best we can do
    physical, logical = test_me
    assert physical >= 1
    assert logical >= physical
    assert logical % physical == 0
