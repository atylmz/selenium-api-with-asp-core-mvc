
using CarProject.UI.Models;
using CarProject.UI.Provider;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace CarProject.UI.Controllers
{
    public class CarController : Controller
    {
        static IEnumerable<CarDTO> cars;
        CarProvider _pro;
        public CarController(CarProvider pro)
        {
            _pro = pro;
        }
        public async Task<IActionResult> Index()
        {
            if (cars == null)
            {
                cars = await _pro.GetCar();
            }
           
           

            return View(cars);
        }
        [HttpPost]
        public async Task<IActionResult> POST(string color, string brand, string tran)
        {
           if(color == null)
            {
                color = " ";
            }

           if(brand == null)
            {
                brand = " ";
            }
           if(tran == null)
            {
                tran = " ";
            }

            cars = await _pro.GetFilteredCar(brand, color, tran);
            
            
            return RedirectToAction("Index",cars);
        }
    }
}
