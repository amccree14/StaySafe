//
//  CheckViewController.swift
//  stay-safe
//
//  Created by Cristian Gonzales on 7/21/17.
//  Copyright © 2017 Northrop Grumman. All rights reserved.
//

import UIKit

class CheckViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBOutlet weak var foodSwitch: UISwitch!
    @IBOutlet weak var waterSwitch: UISwitch!
    @IBOutlet weak var powerSwitch: UISwitch!
    @IBOutlet weak var shelterSwitch: UISwitch!
    
    @IBAction func nextButton(_ sender: Any) {
        
    }

}
