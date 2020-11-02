import cx_Freeze

executables = [cx_Freeze.Executable("sk invader.py")]

cx_Freeze.setup(
    name="Space Invader",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["background.png","background2.jpg","fighter.png"]}},
    executables = executables
    )