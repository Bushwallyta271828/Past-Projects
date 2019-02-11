CC = g++
PROF = -pg
OTHER = -Wall -O3 -std=c++11
CFLAGS = -c

run: play.o move.o print_board.o insert_randoms.o done.o find_direction.o heuristic.o
	$(CC) $(OTHER) *.o -o run

done.o: done.cpp done.hpp move.hpp
	$(CC) $(CFLAGS) $(OTHER) done.cpp

move.o: move.cpp move.hpp
	$(CC) $(CFLAGS) $(OTHER) move.cpp

print_board.o: print_board.cpp print_board.hpp
	$(CC) $(CFLAGS) $(OTHER) print_board.cpp

heuristic.o: heuristic.cpp heuristic.hpp
	$(CC) $(CFLAGS) $(OTHER) heuristic.cpp

insert_randoms.o: insert_randoms.cpp insert_randoms.hpp
	$(CC) $(CFLAGS) $(OTHER) insert_randoms.cpp

play.o: play.cpp move.hpp print_board.hpp insert_randoms.hpp done.hpp find_direction.hpp
	$(CC) $(CFLAGS) $(OTHER) play.cpp

find_direction.o: find_direction.cpp find_direction.hpp move.hpp insert_randoms.hpp heuristic.hpp
	$(CC) $(CFLAGS) $(OTHER) find_direction.cpp

clean:
	rm -f *.o *~ run
