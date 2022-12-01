#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int greaterUntilNow = 0;

int sumItems(std::vector<int> &array) {
	int sum = 0;
	for (unsigned int i = 0; i < array.size(); i++) {
		sum += array[i];
	}
	
	return sum;
}

int main() {
	std::string b;
	std::ifstream myFile("inputs.txt");
	std::vector<int> arr = {};
	
	while (getline(myFile, b)) {
		if (b == "") {
			int theVeryCoolSum = sumItems(arr);
			if (theVeryCoolSum > greaterUntilNow) {
				greaterUntilNow = theVeryCoolSum;
				// std::cout <<  << std::endl;
			}

			arr.clear();
			continue;
		} else {
			arr.push_back(std::stoi(b));
		}
	}
	
	myFile.close();

	std::cout << greaterUntilNow << std::endl;

	return 0;
}