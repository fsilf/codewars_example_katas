// CodeWars Kata Rank04: Roman Numerals Helper
// Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
// See full description of the kata at: # https://www.codewars.com/kata/51b66044bce5799a7f000003/cpp  

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

class RomanHelper
{
    public:
        std::map<std::string, int>romans = {
            {"M" , 1000},
            {"CM" , 900},
            {"D" , 500},
            {"CD" , 400},
            {"C" , 100},
            {"XC" , 90},
            {"L" , 50},
            {"XL" , 40},
            {"X" , 10},
            {"IX" , 9},
            {"V" , 5},
            {"IV", 4},
            {"I" , 1}
        };
        std::vector<std::string>keys = {
                    "M", "CM", "D", "CD", "C", "XC",
                    "L", "XL", "X", "IX", "V", "IV", "I"};
        std::string to_roman(unsigned int n);
        int         from_roman(std::string rn);

     private:   
        int         _complex_keys(int &res, int &i_key, 
                                    std::string::iterator &it);
        int         _compare_long_keys(std::string key,
                                    std::vector<std::string>l_keys);

} RomanNumerals;

std::string RomanHelper::to_roman(unsigned int n){
    std::string out;

    std::vector<std::string>::iterator it;
    for(it = this->keys.begin(); it != this->keys.end(); it++)
    {
        if (n / romans[*it] > 0)
        {
            int num_times = n / romans[*it];
            for (int i = 0; i < num_times; i++)
            {
                out += *it;
            }
            n = n % romans[*it];
        }
    }
    return out;
}

int    RomanHelper::_complex_keys(int &res, int &i_key, 
                                    std::string::iterator &it)
{
    char first_letter = this->keys[i_key][0];
    char second_letter = this->keys[i_key][1];

    if (*it == first_letter && *(it+1) == second_letter)
    {
        res += this->romans[this->keys[i_key]];
        it++;
        i_key += 1;
        return (1);
    }
    i_key += 1;
    return (0);
}

int     RomanHelper::_compare_long_keys(std::string key,
                                   std::vector<std::string>l_keys)
{
    for(auto& str : l_keys)
    {
        if (!key.compare(str))
            return (1);
    }
    return (0);
}

int         RomanHelper::from_roman(std::string rn){
    int res = 0;
    int i_key = 0;
    std::vector<std::string> l_keys = {
                    "CM", "CD", "XC", "XL","IX", "IV"};

    for(std::string::iterator it = rn.begin(); it != rn.end(); it++)
    {
        while(1)
        {
            if (this->_compare_long_keys(this->keys[i_key], l_keys))
            {
                if (this->_complex_keys(res, i_key, it))
                    break;
            }
            else if (this->keys[i_key][0] == *it)
            {
                res += this->romans[this->keys[i_key]];
                break;
            }
            else
                i_key += 1;
        }
    }
    return res;
}

int main()
{
    
    std::cout << RomanNumerals.to_roman(1990) << std::endl;
    std::cout << RomanNumerals.to_roman(2447) << std::endl;
    std::cout << RomanNumerals.from_roman("XXI") << std::endl;
    std::cout << RomanNumerals.from_roman("MDCLXVI") << std::endl;
    std::cout << RomanNumerals.from_roman("MDCLXIV") << std::endl;
    return(0);
}
