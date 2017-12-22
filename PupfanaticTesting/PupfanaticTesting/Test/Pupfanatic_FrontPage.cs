using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using NUnit.Framework;
using OpenQA.Selenium.Chrome;
using PupfanaticTesting_TestAction;
using OpenQA.Selenium;

namespace PupfanaticTesting
{
    
    [TestFixture]
    public class PupfanaticTesting
    {
        IWebDriver driver = new ChromeDriver();

        [SetUp]
        public void Initialize()
        {
            driver.Navigate().GoToUrl("https://pupfanatic.com");
        }

        [Test, Order(1)]
        public void Verify_Tshirt_Price_Equal_To_Declared_Price()
        {
            PupfanaticTesting_TestAction.PupfanaticTesting_TestAction.Compare_Prices(driver);
        }




        [TearDown]
        public void CleanUp()
        {
            driver.Dispose();
        }
    }
}
