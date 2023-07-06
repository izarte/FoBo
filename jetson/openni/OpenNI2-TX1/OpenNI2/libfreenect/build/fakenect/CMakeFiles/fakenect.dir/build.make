# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build

# Include any dependencies generated for this target.
include fakenect/CMakeFiles/fakenect.dir/depend.make

# Include the progress variables for this target.
include fakenect/CMakeFiles/fakenect.dir/progress.make

# Include the compile flags for this target's objects.
include fakenect/CMakeFiles/fakenect.dir/flags.make

fakenect/CMakeFiles/fakenect.dir/fakenect.c.o: fakenect/CMakeFiles/fakenect.dir/flags.make
fakenect/CMakeFiles/fakenect.dir/fakenect.c.o: ../fakenect/fakenect.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object fakenect/CMakeFiles/fakenect.dir/fakenect.c.o"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/fakenect.dir/fakenect.c.o   -c /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/fakenect/fakenect.c

fakenect/CMakeFiles/fakenect.dir/fakenect.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/fakenect.dir/fakenect.c.i"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/fakenect/fakenect.c > CMakeFiles/fakenect.dir/fakenect.c.i

fakenect/CMakeFiles/fakenect.dir/fakenect.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/fakenect.dir/fakenect.c.s"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/fakenect/fakenect.c -o CMakeFiles/fakenect.dir/fakenect.c.s

fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.requires:

.PHONY : fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.requires

fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.provides: fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.requires
	$(MAKE) -f fakenect/CMakeFiles/fakenect.dir/build.make fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.provides.build
.PHONY : fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.provides

fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.provides.build: fakenect/CMakeFiles/fakenect.dir/fakenect.c.o


fakenect/CMakeFiles/fakenect.dir/parson.c.o: fakenect/CMakeFiles/fakenect.dir/flags.make
fakenect/CMakeFiles/fakenect.dir/parson.c.o: ../fakenect/parson.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object fakenect/CMakeFiles/fakenect.dir/parson.c.o"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/fakenect.dir/parson.c.o   -c /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/fakenect/parson.c

fakenect/CMakeFiles/fakenect.dir/parson.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/fakenect.dir/parson.c.i"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/fakenect/parson.c > CMakeFiles/fakenect.dir/parson.c.i

fakenect/CMakeFiles/fakenect.dir/parson.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/fakenect.dir/parson.c.s"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/fakenect/parson.c -o CMakeFiles/fakenect.dir/parson.c.s

fakenect/CMakeFiles/fakenect.dir/parson.c.o.requires:

.PHONY : fakenect/CMakeFiles/fakenect.dir/parson.c.o.requires

fakenect/CMakeFiles/fakenect.dir/parson.c.o.provides: fakenect/CMakeFiles/fakenect.dir/parson.c.o.requires
	$(MAKE) -f fakenect/CMakeFiles/fakenect.dir/build.make fakenect/CMakeFiles/fakenect.dir/parson.c.o.provides.build
.PHONY : fakenect/CMakeFiles/fakenect.dir/parson.c.o.provides

fakenect/CMakeFiles/fakenect.dir/parson.c.o.provides.build: fakenect/CMakeFiles/fakenect.dir/parson.c.o


fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o: fakenect/CMakeFiles/fakenect.dir/flags.make
fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o: ../src/registration.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/fakenect.dir/__/src/registration.c.o   -c /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/src/registration.c

fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/fakenect.dir/__/src/registration.c.i"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/src/registration.c > CMakeFiles/fakenect.dir/__/src/registration.c.i

fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/fakenect.dir/__/src/registration.c.s"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/src/registration.c -o CMakeFiles/fakenect.dir/__/src/registration.c.s

fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.requires:

.PHONY : fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.requires

fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.provides: fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.requires
	$(MAKE) -f fakenect/CMakeFiles/fakenect.dir/build.make fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.provides.build
.PHONY : fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.provides

fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.provides.build: fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o


# Object files for target fakenect
fakenect_OBJECTS = \
"CMakeFiles/fakenect.dir/fakenect.c.o" \
"CMakeFiles/fakenect.dir/parson.c.o" \
"CMakeFiles/fakenect.dir/__/src/registration.c.o"

# External object files for target fakenect
fakenect_EXTERNAL_OBJECTS =

lib/fakenect/libfakenect.so.0.6.0: fakenect/CMakeFiles/fakenect.dir/fakenect.c.o
lib/fakenect/libfakenect.so.0.6.0: fakenect/CMakeFiles/fakenect.dir/parson.c.o
lib/fakenect/libfakenect.so.0.6.0: fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o
lib/fakenect/libfakenect.so.0.6.0: fakenect/CMakeFiles/fakenect.dir/build.make
lib/fakenect/libfakenect.so.0.6.0: fakenect/CMakeFiles/fakenect.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking C shared library ../lib/fakenect/libfakenect.so"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fakenect.dir/link.txt --verbose=$(VERBOSE)
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && $(CMAKE_COMMAND) -E cmake_symlink_library ../lib/fakenect/libfakenect.so.0.6.0 ../lib/fakenect/libfakenect.so.0.6 ../lib/fakenect/libfakenect.so

lib/fakenect/libfakenect.so.0.6: lib/fakenect/libfakenect.so.0.6.0
	@$(CMAKE_COMMAND) -E touch_nocreate lib/fakenect/libfakenect.so.0.6

lib/fakenect/libfakenect.so: lib/fakenect/libfakenect.so.0.6.0
	@$(CMAKE_COMMAND) -E touch_nocreate lib/fakenect/libfakenect.so

# Rule to build all files generated by this target.
fakenect/CMakeFiles/fakenect.dir/build: lib/fakenect/libfakenect.so

.PHONY : fakenect/CMakeFiles/fakenect.dir/build

fakenect/CMakeFiles/fakenect.dir/requires: fakenect/CMakeFiles/fakenect.dir/fakenect.c.o.requires
fakenect/CMakeFiles/fakenect.dir/requires: fakenect/CMakeFiles/fakenect.dir/parson.c.o.requires
fakenect/CMakeFiles/fakenect.dir/requires: fakenect/CMakeFiles/fakenect.dir/__/src/registration.c.o.requires

.PHONY : fakenect/CMakeFiles/fakenect.dir/requires

fakenect/CMakeFiles/fakenect.dir/clean:
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect && $(CMAKE_COMMAND) -P CMakeFiles/fakenect.dir/cmake_clean.cmake
.PHONY : fakenect/CMakeFiles/fakenect.dir/clean

fakenect/CMakeFiles/fakenect.dir/depend:
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/fakenect /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/fakenect/CMakeFiles/fakenect.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : fakenect/CMakeFiles/fakenect.dir/depend

