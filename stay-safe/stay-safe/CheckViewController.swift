//
//  CheckViewController.swift
//  stay-safe
//
//  Created by Cristian Gonzales on 7/21/17.
//  Copyright © 2017 Northrop Grumman. All rights reserved.
//

import UIKit

class CheckViewController: UIViewController {

    // If bools are initialized to true, then the value is changed
    var foodBool:Bool = false
    var waterBool:Bool = false
    var powerBool:Bool = false
    var shelterBool:Bool = false
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func foodSwitch(_ sender: Any) {
        foodBool = !foodBool
        // Debugging
        print(foodBool)
        
    }
    
    @IBAction func waterSwitch(_ sender: Any) {
        waterBool = !waterBool
        // Debugging
        print(waterBool)
    }
    
    @IBAction func powerSwitch(_ sender: Any) {
        powerBool = !powerBool
        // Debugging
        print(powerBool)
    }
    
    @IBAction func shelterSwitch(_ sender: Any) {
        shelterBool = !shelterBool
        // Debugging
        print(shelterBool)
    }
    
    
    @IBAction func nextButton(_ sender: Any) {
        // Store to DB
        
    }

}
