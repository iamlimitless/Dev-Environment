#include "NetworkNode.h"

NetworkNode::NetworkNode(int id)
{
}

NetworkNode::~NetworkNode(); 
{
}

void NetworkNode::CheckEvents(const unsigned long currentTick)
{
}

void NetworkNode::ResetNode(); 
{
}

void NetworkNode::SetState(NetworkState state)
{
}

void NetworkNode::CheckArrival(const unsigned long currentTick)
{
}

void NetworkNode::SenseMedium(); 
{
}

void NetworkNode::HandlePersistence(); 
{
}

void NetworkNode::HandleCollision(const unsigned long currentTick)
{
}

void NetworkNode::CheckDeparture(const unsigned long currentTick)
{
}

void NetworkNode::StartTransmission(const unsigned long currentTick)
{
}

void NetworkNode::TransmissionComplete(const unsigned long currentTick)
{
}

void NetworkNode::PropogateSignal(const unsigned long currentTick)
{
}

unsigned long NetworkNode::CalcWaitTicks(); 
{
}

