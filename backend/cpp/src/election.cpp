#pragma once
#include ".\election.h"
#include<iostream>
#include <string>
#include <vector>

using namespace std;


Voter::Voter(string first, string second, string third, string fourth, string fifth) {
    firstChoice = first;
    secondChoice = second;
    thirdChoice = third;
    fourthChoice = fourth;
    fifthChoice = fifth;
}


Election::Election(string country, vector<string> parties) {
    this->country = country;
    this->parties = parties;
}

