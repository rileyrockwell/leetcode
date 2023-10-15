# include <iostream>

using namespace std;

# include <unordered_map>
# include <unordered_set>
# include <vector>


int numberOfSubarrays(vector<int>& nums, int k) {
            unordered_map<int, int> counts;
            counts[0] = 1;
            int ans = 0, curr = 0;
            
            for (int num: nums) {
                curr += num % 2;
                ans += counts[curr - k];
                counts[curr] += 1;
            }
            
            return ans;
        }

int main(){
    cout << "testing";
}