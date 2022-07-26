

#include <vector>
#include <iostream>

using std::vector; 
using std::cout;
using std::endl; 


class MaxHeap {
    private: 
        int _size{};
        vector<int> vect = {-1};

        // Function for finding the parent of a node,
        // given an index. This is done by simply 
        // dividing by 2, i.e. bitshifting the 
        // number to the right by one
        int p(int i) {return i>>1;}; 

        int l(int i) {return i<<1;}; // Finding the left node

        int r(int i) {return (i<<1) + 1;}; // Finding the right node

    public:
        bool isEmpty() const {return _size == 0;}; 
        int getMax() const {return vect[0];}; 
        void insertItem(int val);
        void shiftUp(int i);
        int extractMax();
        void shiftDown(int i); 
};

    void MaxHeap::shiftUp(int i) {
        if (i > _size) return;  
        if (i == 1) return; 
        if (vect[i] > p(i)) {
            std::swap(vect[p(i)], vect[i]); 
        }
        shiftUp(p(i)); 

    }

    void MaxHeap::shiftDown(int i) {
        if (i > _size) return; 
        int swapId = i; 

        if (l(i) <= _size && vect[i] < vect[l(i)]) {
            swapId = l(i); 
        }

        if (r(i) <= _size && vect[swapId] < vect[r(i)]) {
            swapId = r(i); 
        }
        
        if (swapId != i) {
            std::swap(vect[i], vect[swapId]); 
            shiftDown(swapId); 
        }
        return; 
    }

    int MaxHeap::extractMax() {
        int maxNum = vect[1]; 
        std::swap(vect[1], vect[_size--]);
        shiftDown(1); 
        return maxNum; 
    }

    void MaxHeap::insertItem(int val) {
        if (_size >= vect.size()) {
            vect.push_back(0); // Placeholder item
        }
        vect[++_size] = val;
        shiftUp(_size); // Moving the item from to back to its proper position
        return; 
    }

int main() {
    MaxHeap* priorityQueue = new MaxHeap(); 
    if (priorityQueue->isEmpty()) {
        cout << "This is the correct answer" << endl; 
    }
    return 0; 

}

