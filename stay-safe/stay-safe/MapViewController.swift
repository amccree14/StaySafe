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
        // Boiler plate for now...
        
        // Create a GMSCameraPosition that tells the map to display the
        // coordinate -33.86,151.20 at zoom level 6.
        let camera = GMSCameraPosition.camera(withLatitude: -33.86, longitude: 151.20, zoom: 6.0)
//        let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
        let rect = CGRect(origin: CGPoint(x: 0,y :0), size: CGSize(width: 100, height: 100))
//        let mapView = GMSMapView.map(withFrame: CGRectMake(0, 0, 100, 100), camera: camera)
        let mapView = GMSMapView.map(withFrame: rect, camera: camera)

        mapView.isMyLocationEnabled = true
        self.view = mapView
        
        // Creates a marker in the center of the map.
        let marker = GMSMarker()
        marker.position = CLLocationCoordinate2D(latitude: -33.86, longitude: 151.20)
//        marker.title = "Sydney"
//        marker.snippet = "Australia"
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
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
