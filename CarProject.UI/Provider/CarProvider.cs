
using CarProject.UI.Models;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;

namespace CarProject.UI.Provider
{
    public class CarProvider
    {
        HttpClient _client;
        public CarProvider(HttpClient client)
        {
            _client=client;
        }
        public async Task<IEnumerable<CarDTO>> GetCar()
        {
            var value = await _client.GetAsync("/cars");

            if (value.IsSuccessStatusCode)
            {
                var content = await value.Content.ReadAsStringAsync();
                var data = JsonConvert.DeserializeObject<IEnumerable<CarDTO>>(content);
                return data;
            }
            return null;
       
        }
        public async Task<IEnumerable<CarDTO>> GetFilteredCar(string brand, string color, string tran)
        {
            var value = await _client.GetAsync($"/filter/{color}/{brand}/{tran}");
            if (value.IsSuccessStatusCode)
            {
                var content = await value.Content.ReadAsStringAsync();
                var data = JsonConvert.DeserializeObject<IEnumerable<CarDTO>>(content);
                return data;
            }
            return null;
        }
    }
}
