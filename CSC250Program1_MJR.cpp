/*
Michael Ryan
1/25/2023
CSC 250
Programming Assignment 1
Write a program that allows the user to enter a team’s ID and displays the number of hits for that team.
You must use the binary search algorithm studied in Unit 1 in this program.
*/

#include <fstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
using namespace std;

const int SIZE = 50;


// read all 3 arrays from the data file, return number of lines read
void readData(int id[], int hits[], int times_hit[], int max_items);

// sort arrays into ascending numerical order according to team ID’s
void sortArray(int id[], int hits[], int times_hit[], int max_items);

// read the user’s choice to see if they want to quit or find team information
int readUserID();

// use the binary search method to find if the user’s choice was in the ID array or not; if not, it’ll return -1.
int binarySearch(int id[], int num_items, int search_value);

// printing the results of the team that the user chose.
void printResults(int id[], int hits[], int times_hit[], int teamID);

int main()
{
    int id[SIZE];
    int hits[SIZE];
    int times_hit[SIZE];
    int quit = 0;
    int searchValue;
    int teamID;

    readData(id, hits, times_hit, SIZE);

    sortArray(id, hits, times_hit, SIZE);

    // loop with menu that asks the user if they want to continue or quit
    while(quit == 0)
    {
        searchValue = readUserID();

        if(searchValue == 2)
        {
            quit = 1;
        }
        else
        {
            teamID = binarySearch(id, SIZE, searchValue);

            if(teamID >= 0)
            {
                printResults(id, hits, times_hit, teamID);
            }
            else
                cout << "\nTeam ID not found, please try again.\n\n";
        }
    }

return 0;
}

void readData(int id[], int hits[], int times_hit[], int max_items)
{
    ifstream inFile;
    int i = 0;

    inFile.open("snowball.txt");
    if(!inFile)
    {
        cout << "Error opening snowball.txt\n";
        exit(23);
    }

    while(i < max_items && inFile >> id[i] >> hits[i] >> times_hit[i])
    {
        i++;
    }

    inFile.close();
    return;
}

void sortArray(int id[], int hits[], int times_hit[], int max_items)
{
    int small_loc;

    // outer loop for the wall
    for(int wall = 0; wall < max_items - 1; wall++)
    {
        // move through unsorted items and find location of smallest
        small_loc = wall;

        for(int loc = wall + 1; loc < max_items; loc++)
        {
            if(id[loc] < id[small_loc])
            {
                small_loc = loc;
            }
        }
        // smallest value is at location small_loc, swap it
        // with the value at location small
        swap(id[small_loc], id[wall]);
        swap(hits[small_loc], hits[wall]);
        swap(times_hit[small_loc], times_hit[wall]);
    }
    return;
}

int readUserID()
{
    int choice;

    cout << "Enter Team ID or press 2 and return to quit: ";
    cin >> choice;

    return choice;
}

int binarySearch(int id[], int num_items, int search_value)
{
    int middle_loc;
    int first, last;
    int position = -1;

    first = 0;
    last = num_items - 1;

    while(position == -1 && first <= last)
    {
        // find the middle location
        middle_loc = (first + last) / 2;

        if(search_value > id[middle_loc])
        {
            first = middle_loc + 1;
        }
        else if(search_value < id[middle_loc])
        {
            last = middle_loc - 1;
        }
        else
            position = middle_loc;
    }
    return position;
}

void printResults(int id[], int hits[], int times_hit[], int teamID)
{
    cout << "\nTeam ID:" << setw(10) << id[teamID]
    << endl << "Hits:" << setw(13) << hits[teamID]
    << endl << "Times Hit:" << setw(8) << times_hit[teamID] << endl << endl;

    if(hits[teamID] > times_hit[teamID])
    {
        cout << "Congratulations!!!\n\n";
    }
    return;
}

void selectionSort(int id[], int num_size)
{
    int small_loc;

    for(int wall = 0; wall < num_size; wall++)
    {
        small_loc = wall;
        for(int loc = wall + 1; loc < num_size; loc++)
        {
            if(id[small_loc] > id[loc])
            {
                small_loc = loc;
            }
        }
        swap(id[small_loc], id[wall]);
    }
}


