#ifndef PID_H
#define PID_H
namespace brewcontrol
{

class PID{
	public:

		// Constructor
		PID (float kp, float ki, float kd);
		~PID ();
		// Compute
		float compute(float error);
		void setNewSetpoint(float setPoint);
		void schedule(int millis);

		// Properties
		float kp() const {return _kp; }
		void kp(const float kp) { _kp = kp; }
		float ki() const {return _ki; }
		void ki(const float ki) { _ki = ki; }
		float kd() const {return _kd; }
		void kd(const float kd) { _kd = kd; }

		float setPoint() const { return _setPoint; } 
    	void setPoint(const float setPoint) { _setPoint = setPoint; }
	private:
	 	float _kp;
		float _ki;
		float _kd;

		float _setPoint;
		float _sumError;

		float _previousError;
		int _lastComputation;

		int _scheduleMillis;
};

}

#endif