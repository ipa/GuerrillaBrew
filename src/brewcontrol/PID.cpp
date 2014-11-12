#include "PID.hpp"

using namespace brewcontrol;

PID::PID(float kp, float ki, float kd){
    _kp = kp;
    _ki = ki;
    _kd = kd;

    _sumError = 0;
    _previousError = 0;
    _lastComputation = 0;
}

PID::~PID (){

}

float PID::compute(float error){
    return 0;
}

void PID::setNewSetpoint(float setPoint){

}

void PID::schedule(int millis){

}