//
// Created by wangwei on 2019/10/13.
//

#include <iostream>
#include <vector>
using namespace std;

class Subject;

class Observer {
public:
    virtual ~Observer() {}
    virtual int getState() = 0;
    virtual void update(Subject *subject) = 0;
}; // class Observer

class ConcreteObserver : public Observer {
public:
    ConcreteObserver(const int state):observer_state(state) {}
    ~ConcreteObserver() {}

    int getState(){
        return observer_state;
    }

    void update(Subject *subject);

private:
    int observer_state;
}; // class ConcreteObserver

class Subject {
public:
    virtual ~Subject() {}
    void attach(Observer *ob){
        observers.push_back(ob);
    }

    void detach(const int index){
        observers.erase(observers.begin() + index);
    }

    void notify(){
        for(auto it : observers){
            it->update(this);
        }
    }

    virtual int getState() = 0;
    virtual void setState(const int s) = 0;

private:
    std::vector<Observer*> observers;
}; // class Subject

class ConcreteSubject : public Subject {
public:
    ~ConcreteSubject() {}
    int getState() override {
        return subject_state;
    }

    void setState(const int s){
        subject_state = s;
    }

private:
    int subject_state;
};

void ConcreteObserver::update(Subject *subject) {
    observer_state = subject->getState();
    cout << "Observer state updated." << endl;
}

int main(){
    ConcreteObserver observer1(1);
    ConcreteObserver observer2(2);

    cout << "Observer 1 state: " << observer1.getState() << endl;
    cout << "Observer 2 state: " << observer2.getState() << endl;

    Subject *subject = new ConcreteSubject();
    subject->attach(&observer1);
    subject->attach(&observer2);
    subject->setState(10);
    subject->notify();

    cout << "Observer 1 state: " << observer1.getState() << endl;
    cout << "Observer 2 state: " << observer2.getState() << endl;

    delete subject;

    return 0;
}
