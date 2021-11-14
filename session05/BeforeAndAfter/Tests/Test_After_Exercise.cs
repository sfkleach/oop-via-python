using Microsoft.VisualStudio.TestTools.UnitTesting;
#nullable enable

namespace Tests.After
{
    using System.Collections.Generic;
    using System.Linq;
    using BeforeAndAfter.After;

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
            var ts = Exercise.FilterProposals(dataToFilter, filter, tab)?.ToList();
            //  Assert
            Assert.IsNotNull(ts);
            Assert.AreEqual(0, ts.Count);
        }

        [TestMethod]
        public void Empty_Test_FilterProposals()
        {
            //  Arrange
            IEnumerable<Article> dataToFilter = Enumerable.Empty<Article>();
            UserFilter? filter = null;
            TabEnum tab = TabEnum.Accepted;
            //  Act
            var ts = Exercise.FilterProposals(dataToFilter, filter, tab)?.ToList();
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
                new Article("Article1") { ReviewCode = 0, HiddenByReviewer = false },
                new Article("Article2") { ReviewCode = 1, HiddenByReviewer = true }
            };
            UserFilter? filter = null;
            TabEnum tab = TabEnum.Accepted;
            //  Act
            var ts = Exercise.FilterProposals(dataToFilter, filter, tab)?.ToList();
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
                new Article("Article_A") { ReviewCode = 0, HiddenByReviewer = false },
                new Article("Article_B") { ReviewCode = 1, HiddenByReviewer = false }
            };
            UserFilter filter = new("_B");
            TabEnum tab = TabEnum.Accepted;
            //  Act
            var ts = Exercise.FilterProposals(dataToFilter, filter, tab)?.ToList();
            //  Assert
            Assert.IsNotNull(ts);
            Assert.AreEqual(1, ts.Count);
            Assert.AreEqual("Article_B", ts[0].Name);
        }
    }
}
