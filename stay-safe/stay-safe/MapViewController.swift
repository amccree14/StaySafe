//
//  MapViewController.swift
//  stay-safe
//
//  Created by Cristian Gonzales on 7/21/17.
//  Copyright © 2017 Northrop Grumman. All rights reserved.
//

import UIKit
import GoogleMaps

class MapViewController: UIViewController {

    override func loadView() {
        
        let camera = GMSCameraPosition.camera(withLatitude: 33.83269, longitude: -118.3272286, zoom: 2.0)
        let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
//        mapView.isMyLocationEnabled = true
//        self.view.addSubview(mapView)
//        mapView = GMSMapView.map(withFrame: self.view.bounds, camera: camera)
//        self.view.addSubview(mapView)
        view = mapView
        
        // Creates a marker in the center of the map.
        let marker = GMSMarker()
        marker.position = CLLocationCoordinate2D(latitude: 33.83269, longitude: -118.3272286)
        marker.map = mapView
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}
