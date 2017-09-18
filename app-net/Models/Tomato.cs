using System;
using System.ComponentModel.DataAnnotations;

namespace phone_api.Models
{
    public class Tomato
    {
        [Key]
        public int Id { get; set; }
        [Required]
        [MaxLength(20)]
        public string Name { get; set; }
    }
}
