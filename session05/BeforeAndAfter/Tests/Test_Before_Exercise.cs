using Microsoft.VisualStudio.TestTools.UnitTesting;
#nullable enable

namespace Tests.Before
{
    using System.Collections.Generic;
    using System.Linq;
    using BeforeAndAfter.Before;

    [TestClass]
    public class Basic_Test_Exercise
    {
        [TestMethod]
        public void Null_Test_FilterProposals()
        {
            //  Arrange
            IEnumerable<Article> dataToFilter = Enumerable.Empty<Article>();
            UserFilter? filter = null;
            TabEnum tab = TabEnum.WorkInProgress;
            //  Act
            var ts = new Exercise().FilterProposals(dataToFilter, filter, tab)?.ToList();
            //  Assert
            Assert.IsNull(ts);
        }

        [TestMethod]
        public void Empty_Test_FilterProposals()
        {
            //  Arrange
            IEnumerable<Article> dataToFilter = Enumerable.Empty<Article>();
            UserFilter? filter = null;
            TabEnum tab = TabEnum.Accepted;
            //  Act
            var ts = new Exercise().FilterProposals(dataToFilter, filter, tab)?.ToList();
            //  Assert
            Assert.IsNotNull(ts);
            Assert.AreEqual(0, ts.Count);
        }

        [TestMethod]
        public void Filter_1_Test_FilterProposals()
        {
            //  Arrange
            IEnumerable<Article> dataToFilter = new List<Article>()
            {
                new Article() {Name = "Article1", ReviewCode = 0, HiddenByReviewer = false },
                new Article() {Name = "Article2", ReviewCode = 1, HiddenByReviewer = true }
            };
            UserFilter? filter = null;
            TabEnum tab = TabEnum.Accepted;
            //  Act
            var ts = new Exercise().FilterProposals(dataToFilter, filter, tab)?.ToList();
            //  Assert
            Assert.IsNotNull(ts);
            Assert.AreEqual(1, ts.Count);
            Assert.AreEqual("Article1", ts[0].Name);
        }

        [TestMethod]
        public void UserFilter_1_Test_FilterProposals()
        {
            //  Arrange
            var dataToFilter = new List<Article>()
            {
                new Article() {Name = "Article_A", ReviewCode = 0, HiddenByReviewer = false },
                new Article() {Name = "Article_B", ReviewCode = 1, HiddenByReviewer = false }
            };
            UserFilter filter = new() { Logic = "or", Operator = "contains", Value = "1" };
            TabEnum tab = TabEnum.Accepted;
            //  Act
            var ts = new Exercise().FilterProposals(dataToFilter, filter, tab)?.ToList();
            //  Assert
            Assert.IsNotNull(ts);
            Assert.AreEqual(1, ts.Count);
            Assert.AreEqual("Article_B", ts[0].Name);
        }
    }
}
