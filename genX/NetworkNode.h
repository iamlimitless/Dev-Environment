#ifndef NETWORK_NODE_H
#define NETWORK_NODE_H

class NetworkQueue;
class NetworkNode;

extern double gPersistenceParam;
extern double gArrivalRate;
extern unsigned int gNumNodes;
extern unsigned int gPacketsProcessed;
extern unsigned int gPacketDelay;
extern unsigned int gDropCount;
extern NetworkNode ** gNodeList;

enum NetworkState
{
    MediumIdle = 0,
    MediumBusy, //1
    CollisionDetected, //2
    Transmitting, //3
    Jamming, //4
    Persistence
};

class NetworkNode
{
public:

    NetworkNode(int id);
    ~NetworkNode();

    void CheckEvents(const unsigned long currentTick);
    void ResetNode();
    NetworkState GetState() { return mState; }
    void SetState(NetworkState state);

    bool operator==(const NetworkNode& other) const
    {
        return false;
    }

private:

    void CheckArrival(const unsigned long currentTick);
    void SenseMedium();
    void HandlePersistence();
    void HandleCollision(const unsigned long currentTick);
    void CheckDeparture(const unsigned long currentTick);
    
    void StartTransmission(const unsigned long currentTick);
    void TransmissionComplete(const unsigned long currentTick);
    void PropogateSignal(const unsigned long currentTick);

    unsigned long CalcWaitTicks();

    //Data Members
    NetworkQueue *mNetQueue;
    const int mNodeId;
    int mRetryCount;
    unsigned int mWaitCount;
    unsigned long mNextArrivalTick;
    unsigned long mSignalStartTick;
    NetworkState mState;
};

#endif
