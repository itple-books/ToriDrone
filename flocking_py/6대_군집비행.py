from time import sleep

# 코딩 라이더 모듈 불러오기
from CodingRider.drone import *
from CodingRider.protocol import *

# 메인 실행 부분
if __name__ == '__main__':
    
    drone1 = Drone()    # 1번째 Drone 객체 생성 후 변수(drone1)에 저장
    drone2 = Drone()    # 2번째 Drone 객체 생성 후 변수(drone2)에 저장
    drone3 = Drone()    # 3번째 Drone 객체 생성 후 변수(drone3)에 저장
    drone4 = Drone()    # 4번째 Drone 객체 생성 후 변수(drone4)에 저장
    drone5 = Drone()    # 5번째 Drone 객체 생성 후 변수(drone5)에 저장
    drone6 = Drone()    # 6번째 Drone 객체 생성 후 변수(drone6)에 저장
    
# 연결된 각 드론과의 통신을 위한 시리얼 포트 연결 작업
    drone1.open("COM13")    # drone1 시리얼 포트 연결
    drone2.open("COM12")    # drone2 시리얼 포트 연결
    drone3.open("COM7")    # drone3 시리얼 포트 연결
    drone4.open("COM8")    # drone4 시리얼 포트 연결  
    drone5.open("COM18")    # drone5 시리얼 포트 연결  
    drone6.open("COM9")    # drone6 시리얼 포트 연결
    sleep(0.1)
    
    print("Accel, Gyro Bias 초기화")
    for i in range(30) :
        drone1.sendClearBias()
        drone2.sendClearBias()
        drone3.sendClearBias()
        drone4.sendClearBias()
        drone5.sendClearBias()
        drone6.sendClearBias()
    sleep(0.2)
    
    print("비행, 주행 Trim 초기화")
    for i in range(30) :
        drone1.sendClearTrim()
        drone2.sendClearTrim()
        drone3.sendClearTrim()
        drone4.sendClearTrim()
        drone5.sendClearTrim()
        drone6.sendClearTrim()
    sleep(0.2)
    
    print("군집 전용 드론고도제어 설정")
    for i in range(30) :
        drone1.sendSetSwarm()
        drone2.sendSetSwarm()
        drone3.sendSetSwarm()
        drone4.sendSetSwarm()
        drone5.sendSetSwarm()
        drone6.sendSetSwarm()
    sleep(0.2)    
    
    print("led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
    sleep(0.2)
        
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
    sleep(0.2)
    
    #4초 대기
    for i in range(2, 0, -1) :
        print("{0}".format(i))
        sleep(1)
        
    # 456 이륙
    print("456 TakeOff")
    for i in range(30) :
        drone4.sendTakeOff()    # drone4 이륙
        drone5.sendTakeOff()    # drone5 이륙
        drone6.sendTakeOff()    # drone6 이륙
    sleep(3.9)
        
    # 123 이륙
    print("123 TakeOff")
    for i in range(30) :
        drone1.sendTakeOff()    # drone1 이륙
        drone2.sendTakeOff()    # drone2 이륙
        drone3.sendTakeOff()    # drone3 이륙
    sleep(5.7)
    

    print("1/3/4/6 위치 이동")
    for i in range(30) :
        drone1.sendControlPosition(-1.5, 0.5, 0, 0.6, 0, 0)
        drone3.sendControlPosition(-1.5, -0.5, 0, 0.6, 0, 0)
        drone4.sendControlPosition(0, -0.5, 0, 0.5, 0, 0)
        drone6.sendControlPosition(0, 0.5, 0, 0.5, 0, 0)
    sleep(3.9)
    
    print("전체 LED 변경(보라)")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
    sleep(0.1)
    #V자 비행
    print("V자 비행")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone2.sendControlPosition(0, 0, 0.4, 0.4, 0, 0)
        drone3.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone4.sendControlPosition(0, 0, 0.4, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, 0.4, 0.4, 0, 0)
    sleep(3.7)
    
    print("원상태로 돌아오기")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
        drone3.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
        drone4.sendControlPosition(0, 0, -0.4, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, -0.4, 0.4, 0, 0)
    sleep(3.9)
    
    #V자 비행
    print("역 V자 비행")
    for i in range(30) :
        drone4.sendControlPosition(0, 0, 0.4, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, 0.4, 0.4, 0, 0)
        drone5.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
    sleep(3.9)
    
    print("원상태로 돌아오기")
    for i in range(30) :
        drone2.sendControlPosition(0, 0, -0.4, 0.4, 0, 0)
        drone4.sendControlPosition(0, 0, -0.4, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, -0.4, 0.4, 0, 0)
        drone5.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
    sleep(3.9)
    
    print("원래 대형으로 돌아오기")
    for i in range(30) :
        drone1.sendControlPosition(1.5, -0.5, 0, 0.6, 0, 0)
        drone3.sendControlPosition(1.5, 0.5, 0, 0.6, 0, 0)
        drone4.sendControlPosition(0, 0.5, 0, 0.5, 0, 0)        
        drone6.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) 
    sleep(3.9)
    
    
    
    #드론 2/5번 행동 제어
    print("드론 2/5번 제어")
    for i in range(30) :
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    for i in range(30) :
        drone2.sendControlPosition(0.7, 0, 0, 0.5, 0, 0)
        drone5.sendControlPosition(0.7, 0, 0, 0.5, 0, 0)
    sleep(3.8)
    
    #드론 1/3/4/6번 제어
    print("드론 1/3/4/6번 제어")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    for i in range(30) :
        drone1.sendControlPosition(0, -0.5, 0, 0.5, 0, 0)
        drone3.sendControlPosition(0, 0.5, 0, 0.5, 0, 0)
        drone4.sendControlPosition(0, 0.5, 0, 0.5, 0, 0)
        drone6.sendControlPosition(0, -0.5, 0, 0.5, 0, 0)
    sleep(3.7)
    
    #드론 전체 상승 비행
    print("전체 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
            
    print("전체 led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    print("전체 상승 비행")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone2.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone3.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone4.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone5.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
    sleep(3.6)
    
    #드론 전체 하강 비행
    print("전체 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
    print("전체 led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    print("전체 하강 비행")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
        drone2.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
        drone3.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
    sleep(3.75)
    
    
    #드론 전체 하강 비행
    print("전체 led 색 변경")
    for i in range(30) :
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
    print("전체 led 다리색 변경")
    for i in range(30) :
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    print("전체 하강 비행")
    for i in range(30) :
        drone4.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
        drone5.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
    sleep(3.75)
    
    #드론 전체 상승 비행
    print("전체 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
    sleep(0.1)
    print("V자 상승 비행")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.4, 0.4, 0, 0)
        drone3.sendControlPosition(0, 0, 0.4, 0.4, 0, 0)
        drone4.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, 0.8, 0.4, 0, 0)
    sleep(3.75)
    
    #드론 전체 하강 비행
    print("전체 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
    sleep(0.1)
    print("V자 하강 비행")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.4, 0.4, 0, 0)
        drone3.sendControlPosition(0, 0, -0.4, 0.4, 0, 0)
        drone4.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
        drone6.sendControlPosition(0, 0, -0.8, 0.4, 0, 0)
    sleep(3.75)
    
    
    #원래 자리로 돌아가기
    print("일괄 색 변경(분홍)")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
    sleep(0.1)
    print("원래자리로 돌아가기")
    for i in range(30) :
        drone1.sendControlPosition(0, 0.5, 0, 0.5, 0, 0)
        drone3.sendControlPosition(0, -0.5, 0, 0.5, 0, 0)  
        drone4.sendControlPosition(0, -0.5, 0, 0.5, 0, 0)
        drone6.sendControlPosition(0, 0.5, 0, 0.5, 0, 0)
        drone2.sendControlPosition(-0.7, 0, 0, 0.5, 0, 0)
        drone5.sendControlPosition(-0.7, 0, 0, 0.5, 0, 0)
    sleep(3.6)
    
    
    print("135 빨 / 246 파 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
    sleep(0.1)         
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(1.75)
        
    print("135 파 / 246 빨 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
    sleep(0.1)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(1.75)
 
    print("135 빨 / 246 파 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
    sleep(0.1)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(1.75)
        
    print("135 파 / 246 빨 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
    sleep(0.1)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(1.75)
    
    print("135 빨 / 246 파 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
    sleep(0.1)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(1.75)
        
    print("135 파 / 246 빨 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
    sleep(0.1)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)  
    sleep(1.75)
    
    print("135 빨 / 246 파 led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
    sleep(0.1)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(1.75)
    
    print("전체 흰색")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 255, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 255, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 255, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 255, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 255, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 255, 255)
    sleep(0.1)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
    sleep(1.75)
    
     #드론 전체 원형 비행
    print("드론 1-6번 단체 원형비행")
    for i in range(30) :
        drone1.sendControlPosition(4.5, 0, 0, 0.75, 360, 60)
        drone2.sendControlPosition(4.5, 0, 0, 0.75, 360, 60)
        drone3.sendControlPosition(4.5, 0, 0, 0.75, 360, 60)
        drone4.sendControlPosition(4.5, 0, 0, 0.75, 360, 60)
        drone5.sendControlPosition(4.5, 0, 0, 0.75, 360, 60)
        drone6.sendControlPosition(4.5, 0, 0, 0.75, 360, 60)
    sleep(7.85)
    
    #드론 전체 원형 비행
    print("드론 1-6번 단체 원형비행(반대)")
    for i in range(30) :
        drone1.sendControlPosition(4.5, 0, 0, 0.75, -360, -60)
        drone2.sendControlPosition(4.5, 0, 0, 0.75, -360, -60)
        drone3.sendControlPosition(4.5, 0, 0, 0.75, -360, -60)
        drone4.sendControlPosition(4.5, 0, 0, 0.75, -360, -60)
        drone5.sendControlPosition(4.5, 0, 0, 0.75, -360, -60)
        drone6.sendControlPosition(4.5, 0, 0, 0.75, -360, -60)
    sleep(7.85)
    
    
        #슬로우 상승비행
    print("3/6 슬로우 상승비행")
    for i in range(30)  :
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)   
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)   
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    for i in range(30) :
        drone3.sendControlPosition(0, 0, 0.6, 0.2, 0, 0)
        drone6.sendControlPosition(0, 0, 0.6, 0.2, 0, 0)
    sleep(1.75)
    
    print("2/5 슬로우 상승비행")
    for i in range(30)  :
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)   
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)   
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    for i in range(30) :
        drone2.sendControlPosition(0, 0, 0.6, 0.2, 0, 0)
        drone5.sendControlPosition(0, 0, 0.6, 0.2, 0, 0)
    sleep(1.75)
    
    print("1/4 슬로우 상승비행")
    for i in range(30)  :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)   
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)   
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.6, 0.2, 0, 0)
        drone4.sendControlPosition(0, 0, 0.6, 0.2, 0, 0)
    sleep(3.75)
    
    #슬로우 하강비행
    print("3/6 슬로우 하강비행")
    for i in range(30)  :
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)   
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)   
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone3.sendControlPosition(0, 0, -0.6, 0.2, 0, 0)
        drone6.sendControlPosition(0, 0, -0.6, 0.2, 0, 0)
    sleep(1.75)
    
    print("2/5 슬로우 하강비행")
    for i in range(30)  :
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)   
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)   
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone2.sendControlPosition(0, 0, -0.6, 0.2, 0, 0)
        drone5.sendControlPosition(0, 0, -0.6, 0.2, 0, 0)
    sleep(1.75)
    
    print("1/4 슬로우 하강비행")
    for i in range(30)  :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)   
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)   
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.6, 0.2, 0, 0)
        drone4.sendControlPosition(0, 0, -0.6, 0.2, 0, 0)
    sleep(3.5)
    
    #드론 14 상승
    print("드론 14 상승")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone4.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
    sleep(1.75)
    
    #드론 14하강 25번 상승
    print("드론 14하강 25상승")
    for i in range(30) :
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone2.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone4.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone5.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
    sleep(1.6)    
    
    #드론 25하강 36번 상승
    print("드론 25하강 36상승")
    for i in range(30) :
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone2.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone3.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone5.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone6.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
    sleep(1.6)    
    
    #드론 36 하강
    print("드론 36 하강")
    for i in range(30) :
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone3.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone6.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
    sleep(1.75)
    
    #드론 36 상승
    print("드론 36 상승")
    for i in range(30) :
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    for i in range(30) :
        drone3.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone6.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
    sleep(1.75)
    
    #드론 36하강 25번 상승
    print("드론 36하강 25상승")
    for i in range(30) :
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone2.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone3.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone5.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone6.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
    sleep(1.6)    
    
    #드론 25하강 14번 상승
    print("드론 25하강 14상승")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone2.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone4.sendControlPosition(0, 0, 0.5, 0.5, 0, 0)
        drone5.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
    sleep(1.6)    
    
    #드론 14 하강
    print("드론 14 하강")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
    sleep(0.1)
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
        drone4.sendControlPosition(0, 0, -0.5, 0.5, 0, 0)
    sleep(1.75)
        
    print("전체 제자리 회전")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.4, 0.1, 360, 90)
        drone2.sendControlPosition(0, 0, 0.4, 0.1, 360, 90)
        drone3.sendControlPosition(0, 0, 0.4, 0.1, 360, 90)
        drone4.sendControlPosition(0, 0, 0.4, 0.1, 360, 90)
        drone5.sendControlPosition(0, 0, 0.4, 0.1, 360, 90)
        drone6.sendControlPosition(0, 0, 0.4, 0.1, 360, 90)
    sleep(5.85)
    
    # 착륙하기
    print("Landing")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
    
    for i in range(30) :
        drone1.sendLanding()    # drone1 착륙
        drone2.sendLanding()    # drone2 착륙
        drone3.sendLanding()    # drone3 착륙
        drone4.sendLanding()    # drone4 착륙
        drone5.sendLanding()    # drone5 착륙
        drone6.sendLanding()    # drone6 착륙
        
    for i in range(5, 0, -1):   # 착륙 및 하강하는동안 5초 카운트
        print("{0}".format(i))
        sleep(1)
    

    # 시리얼 포트 닫기 작업(모든 명령이 완료되면 시리얼 포트를 닫아줌.)
    drone1.close()  # drone1 시리얼 포트 닫기
    drone2.close()  # drone2 시리얼 포트 닫기
    drone3.close()  # drone3 시리얼 포트 닫기
    drone4.close()  # drone4 시리얼 포트 닫기
    drone5.close()  # drone5 시리얼 포트 닫기
    drone6.close()  # drone6 시리얼 포트 닫기