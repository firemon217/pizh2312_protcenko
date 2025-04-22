# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-src"
  "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-build"
  "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-subbuild/googletest-populate-prefix"
  "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-subbuild/googletest-populate-prefix/tmp"
  "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-subbuild/googletest-populate-prefix/src/googletest-populate-stamp"
  "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-subbuild/googletest-populate-prefix/src"
  "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-subbuild/googletest-populate-prefix/src/googletest-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-subbuild/googletest-populate-prefix/src/googletest-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Work/University/OOP/pizh2312_protcenko/lab8/out/build/x64-Debug/_deps/googletest-subbuild/googletest-populate-prefix/src/googletest-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
