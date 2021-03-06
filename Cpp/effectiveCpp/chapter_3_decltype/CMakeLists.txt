CMAKE_MINIMUM_REQUIRED( VERSION 3.8 )

PROJECT( MyAnalysisProject )

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/CMakeModules")

SET( PROJECT_VERSION_MAJOR 0 )
SET( PROJECT_VERSION_MINOR 1 )

# FIND_PACKAGE( Boost 1.62 COMPONENTS program_options REQUIRED )
# INCLUDE_DIRECTORIES ( ${Boost_INCLUDE_DIRS})

INCLUDE_DIRECTORIES ( ${PROJECT_SOURCE_DIR}/MyAnalysis/include )


FOREACH( pkg  )
    FIND_PACKAGE (${pkg} REQUIRED )
    IF( ${pkg}_FOUND )
	INCLUDE_DIRECTORIES( SYSTEM ${${pkg}_INCLUDE_DIRS} )
	ADD_DEFINITIONS( ${${pkg}_DEFINITIONS} )
	ADD_DEFINITIONS( -DUSE_${pkg} )
    ENDIF()
ENDFOREACH()

SET( CMAKE_INSTALL_PREFIX ${PROJECT_SOURCE_DIR} )
LIST ( APPEND CMAKE_CXX_FLAGS "-O3 -Wall -Wextra -Wshadow -ansi -Wno-long-long -Wuninitialized -fopenmp -flto -Weffc++ --std=c++14 -ggdb" )
LIST ( APPEND CMAKE_LD_FLAGS "-flto -O3 -ggdb" )

# find_package ( ROOT REQUIRED )
# include(${ROOT_USE_FILE})

ADD_SUBDIRECTORY ( ${PROJECT_SOURCE_DIR}/MyAnalysis )

MESSAGE (STATUS "*** Build Type ${CMAKE_BUILD_TYPE} ***" )
MESSAGE (STATUS "*** Compiler Flags:  ${CMAKE_CXX_FLAGS}"  )
MESSAGE (STATUS "*** Compiler Flags:  ${CMAKE_CXX_FLAGS_DEBUG}"  )

