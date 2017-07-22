//
//  ContactsViewController.swift
//  stay-safe
//
//  Created by Cristian Gonzales on 7/21/17.
//  Copyright © 2017 Northrop Grumman. All rights reserved.
//

import UIKit

class ContactsViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBOutlet weak var firstNameField: UITextField!
    @IBOutlet weak var lastNameField: UITextField!
    @IBOutlet weak var phoneNumField: UITextField!
    
    @IBAction func submitButton(_ sender: Any) {
        
    }

}
