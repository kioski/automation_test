using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using NUnit.Framework;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium;

namespace PupfanaticTesting_TestAction
{

    public class PupfanaticTesting_TestAction
    {

        public static void Compare_Prices(IWebDriver driver)
        {
            driver.FindElement(By.Name("q")).SendKeys("Yes");
            driver.FindElement(By.Name("btnK")).Click();
        }

    }

}
