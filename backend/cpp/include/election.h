#include<iostream>
#include <string>
#include <vector>
#include<unordered_set>
using namespace std;

struct Voter {
        public:
            string firstChoice;
            string secondChoice;
            string thirdChoice;
            string fourthChoice;
            string fifthChoice;

            Voter(string first, string second = "n/a", string third = "n/a", string fourth = "n/a", string fifth = "n/a");

    };

class Election {
    string country;
    int numParties;
    vector<string> parties;
    vector<Voter> voters;

    Election(string country, vector<string> parties);
};
