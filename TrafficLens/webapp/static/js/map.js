function initMap() {
    var mapOptions = {                                              // *** 지도 생성 시 옵션 ***
        center: new naver.maps.LatLng(37.3595704, 127.105399),      // 지도의 초기 중심 좌표
        zoom: 11,                                                   // 지도의 초기 줌 레벨
        mapTypes: new naver.maps.MapTypeRegistry({                  // 일반 지도 배경에 실시간 혼잡 교통 정보 요청
            'normal': naver.maps.NaverStyleMapTypeOptions.getNormalMap(
              {
                overlayType: 'bg.ol.ts.ctt.lko'
              }
            )
        })
    };

    var map = new naver.maps.Map('map', mapOptions);
}